Q: How to copy text from vi to clipboard in OSX terminal

Follow below steps
1.Position the cursor where you want to begin copying.

2.Press v (or upper case V if you want to cut whole lines).

3.Move the cursor to the end of what you want to copy.

4.Type->   :'<,'>w !pbcopy 

Q:Find a text in list of files returned by find:

Solution:
find ./ -name *.csproj -print0 | xargs -0 grep 'Include' | grep Microsoft.Extensions

Explaination:
print0 -> separates the filenames with a 0 (NULL) byte so that names containing spaces or newlines can be interpreted correctly

xargs ->  command reads space- or newline-separated strings (typically from the find command, but they could come from anywhere) and executes some command for each string.
If xargs is run with a -0 option, it'll expect NULL-separated strings as output by
