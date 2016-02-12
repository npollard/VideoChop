package com.nap.videochop;

import java.io.*;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

// http://docs.oracle.com/javase/8/javafx/get-started-tutorial/hello_world.htm
public class VideoChop extends Application {

    @Override
    public void start(Stage primaryStage) {
        final String inputFile = getParameters().getRaw().get(0);
        final VideoChopper videoChopper = new VideoChopper(.2, .5);

        Button chopButton = new Button();
        chopButton.setText("CHOP!");
        chopButton.setOnAction(new EventHandler<ActionEvent>() {
            
            @Override
            public void handle(ActionEvent event) {
                videoChopper.chop(inputFile);
            }
        });
        
        StackPane root = new StackPane();
        root.getChildren().add(chopButton);
        Scene scene = new Scene(root, 100, 100);
        primaryStage.setTitle("VideoChop");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // http://www.javaworld.com/article/2071275/core-java/when-runtime-exec---won-t.html
    private static class StreamGobbler extends Thread {
        InputStream inputStream;
        String type;

        public StreamGobbler(InputStream inputStream, String type) {
            this.inputStream = inputStream;
            this.type = type;
        }

        public void run() {
            ArrayList<String> times = new ArrayList<String>();
            Pattern blackstartPattern = Pattern.compile("black_start:([0-9.]+)");

            try {
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = null;
                while ((line = bufferedReader.readLine()) != null) {
                    System.out.println(type + "> " + line);
                    Matcher blackstartMatcher = blackstartPattern.matcher(line);
                    if (blackstartMatcher.find()) {
                        times.add(line.substring(blackstartMatcher.start(1), blackstartMatcher.end(1)));
                    }
                }
            } catch (IOException e) {
                System.err.println("ERROR: " + e.getLocalizedMessage());
            }

            if (1 < times.size()) {
                for (int i = 0; i < times.size(); i++) {
                    System.out.println("TIMES > " + times.get(i));
                }

                String cmd = "ffmpeg -i " + inputFile + " -ss "; // -ss t1 -c copy -to t2 outputfile
                for (int i = 0; i < times.size() - 1; i++) {
                    System.out.println(cmd + times.get(i) + " -c copy -to " + times.get(i + 1) + " " + inputFile + "." + i);
                }
            }

        }
    }
    
    private static class VideoChopper {
        private double blackDuration, blackThresh;

        public VideoChopper(double blackDuration, double blackThresh) {
            this.blackDuration = blackDuration;
            this.blackThresh = blackThresh;
        }

        public void chop(String inputFile) {
            Runtime runtime = Runtime.getRuntime();
            try {
                String cmd = "ffmpeg -i " + inputFile + " -vf blackdetect=d=" + blackDuration + ":pix_th=" + blackThresh + " -f null -";
                Process blackDetectProc = runtime.exec(cmd);
                StreamGobbler outGobbler = new StreamGobbler(blackDetectProc.getInputStream(), "STDOUT");
                StreamGobbler errGobbler = new StreamGobbler(blackDetectProc.getErrorStream(), "STDERR");
                outGobbler.start();
                errGobbler.start();
                
            } catch (IOException e) {
                System.err.println("ERROR: " + e.getLocalizedMessage());
            }
        }

    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("USAGE: java -jar videochop-2.1.jar [video filename]");
            System.exit(1);
        }

        launch(args);
        
    }

}
