package com.nap.videochop;

import org.bytedeco.javacv.Frame;
import org.bytedeco.javacv.FFmpegFrameGrabber;

public class VideoChop {
    
    private static class VideoChopper {

        public static void chop(String inputFile) {
            FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(inputFile);
            System.out.println(inputFile + ": CHOP!");
        }

    }

    public static void main( String[] args ) {
        VideoChopper.chop("filename");

    }

}
