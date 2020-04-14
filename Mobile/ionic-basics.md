# Ionic Basics

## Pre-requisites
* Install Android Studio
* export ANDROID_HOME=/Users/user/Library/Android/sdk
* export PATH=$PATH/:$NG_HOME/:$MAVEN_HOME/bin:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

## Basic Commands
- Install ionic : `sudo npm install -g ionic`
- List all the information about ionic : `ionic info`
- Generate page structure : `ionic generate page <page-name>`
- If the app crashes after refresh: `npm install @ionic/app-scripts@nightly --save-dev`
- List the cordova requirements: `ionic cordova requirements`
- Run android build and execute: `ionic cordova run android`
- Build for iOS : `ionic cordova build ios`
- Emulate for iOS: `ionic cordova emulate ios`
- Emulate for specific version: `ionic cordova emulate ios --target="<iphone version name>”`
    Eg: `ionic cordova emulate ios --target="iPhone-6”`





