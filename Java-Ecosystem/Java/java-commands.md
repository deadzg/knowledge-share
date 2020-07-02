# List all versions of Java in Mac
`/usr/libexec/java_home -V`

# Find location of specific version of Java
`/usr/libexec/java_home -v 1.8`

# Install specific Java version
https://github.com/AdoptOpenJDK/homebrew-openjdk
`brew tap AdoptOpenJDK/openjdk`
`brew cask install <version>`
Eg: `brew cask install adoptopenjdk11`

# Change JDK
Copy the below code in .bash_profile
```
jdk() {
        version=$1
        export JAVA_HOME=$(/usr/libexec/java_home -v"$version");
        java -version
 }
 ```

 `source ~/.bash_profile`

 `jdk <version>`

 Eg: `jdk 11`


