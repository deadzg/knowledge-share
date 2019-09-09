# Terminal Usage

- Move to the start of the line : `ctrl + A` 
- Move to the end of the line: `ctrl + E` 
- Move forward by word in a line: `esc + F` 
- Move backward by word in a line: `esc + B`

## Find a text in list of files returned by find:
find ./ -name *.csproj -print0 | xargs -0 grep 'Include' | grep Microsoft.Extensions

**Explaination:**
- print0 -> separates the filenames with a 0 (NULL) byte so that names containing spaces or newlines can be interpreted correctly
- xargs ->  command reads space- or newline-separated strings (typically from the find command, but they could come from anywhere) and executes some command for each string.
- If xargs is run with a -0 option, it'll expect NULL-separated strings as output by

## Why I need to source bashrc profile every time I open a terminal for settings to take place
**Explaination**
On most of the platform bash doesnot use .bashrc for login shells. So it reads bash_profile or .profile.
**Solution**
Add `source ~/.bashrc` in your bash_profile
