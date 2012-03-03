let domain_string = read_line ();;

let split_on_dot s = Str.split (Str.regexp_string ".") s;;

let result = split_on_dot domain_string;;

let length = List.length result;;

let compute r = 
  if length < 2 then String.concat "." result
  else ( (List.nth result (length - 2)) ^ "." ^ (List.nth result (length -1)) );;

Printf.printf "%s\n" ( compute result );;
