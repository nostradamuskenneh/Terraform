Numbers:
[[ int1 -eq int2 ]]  or =    -- It return true if they are equal else false
[[ int1 -ne int2 ]]  or !=   -- It return false if they are not equal else true
[[ int1 -lt int2 ]]  or <    -- It return true if int1 is less than int2 else false
[[ int1 -le int2 ]]  or <=   -- It return true if int1 is less than or equal to int2 else false
[[ int1 -gt int2 ]]  or >    -- It return true if int1 is greater than int2 else false
[[ int1 -ge int2 ]]  or >=   -- It return true if int1 is greater than or equal to int2 else false

Strings:
[[ -z str ]]        -- It return true if the length of the str is zero else false
[[ -n str ]]        -- It return true if the length of the str is no-zero else false
[[ str1 == str2 ]]  -- It return true if both the strings are equal else false
[[ str1 != str2 ]]  -- It return true if both the strings are equal else false

File test Operators with test command
[[ -d file ]] -- It return true if the file/path is directory else false
[[ -f file ]] -- It return true if the file/path is a file else false
[[ -e file ]] -- It return true if the file/path is exists else false
[[ -r file ]] -- It return true if the file/path is readable else false
[[ -w file ]] -- It return true if the file/path is writable else false
[[ -x file ]] -- It return true if the file/path is executable else false