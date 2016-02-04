package com.nap.videochop;

import java.io.*;

public class VideoChop {

    // http://www.javaworld.com/article/2071275/core-java/when-runtime-exec---won-t.html
    private static class StreamGobbler extends Thread {
        InputStream inputStream;
        String type;

        public StreamGobbler(InputStream inputStream, String type) {
            this.inputStream = inputStream;
            this.type = type;
        }

        public void run() {
            try {
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = null;
                while ((line = bufferedReader.readLine()) != null) System.out.println(type + "> " + line);
            } catch (IOException e) {
                System.err.println("ERROR: " + e.getLocalizedMessage());
            }
        }
    }
    
    private static class VideoChopper {

        public void chop() {
            Runtime runtime = Runtime.getRuntime();
            try {
                Process blackDetectProc = runtime.exec("ffmpeg -i /home/nelson/Desktop/20160112_161809.mp4 -vf 'blackdetect=d=.2:pix_th=.5' -an -f null -");
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
        VideoChopper videoChopper = new VideoChopper();
        videoChopper.chop();

    }

}
