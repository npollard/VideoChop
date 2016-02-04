package com.nap.videochop;

import java.io.*;

public class VideoChop {

    // http://www.javaworld.com/article/2071275/core-java/when-runtime-exec---won-t.html
    private class StreamGobbler extends Thread {
        InputStream inputStream;
        String type;

        public StreamGobbler(InputStream inputStream, String type) {
            this.inputStream = inputStream;
            this.type = type;
        }

        public void run() {
            try {

            } catch (Exception e) {
                System.err.println("ERROR: " + e.getLocalizedMessage());
            }
        }
    }
    
    private static class VideoChopper {

        public static void chop(String inputFile) {
            Runtime rt = Runtime.getRuntime();
            try {
                rt.exec("ffmpeg -i ~/Desktop/20160112_161809.mp4 -vf 'blackdetect=d=.2:pix_th=.5' -an -f null -");
            } catch (IOException e) {
                System.err.println("ERROR: " + e.getLocalizedMessage());
            }
        }

    }

    public static void main( String[] args ) {
        VideoChopper.chop("filename");

    }

}
