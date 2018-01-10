
# Core.Command

## Status: Resolved

> In the new (0.10) version, what were basic and basic’ have been switched to basic_spec and basic. So you can make your old code work as it was by changing Command.basic into Command.basic_spec. 

> Ref: [Core.Command v.0.10?](https://discuss.ocaml.org/t/core-command-v-0-10/1357)

## Date: 08 Jan 2018

### Error

```
Error: This function has type
         summary:string ->
         ?readme:(unit -> string) ->
         (unit -> unit) Command.Spec.param -> Command.t
       It is applied to too many arguments; maybe you forgot a `;'.
```

### Code 

``` OCaml
(* filename: basic_cmd.ml *)
open Core

let do_hash file =
  In_channel.with_file file ~f:(fun ic ->
      let open Cryptokit in
      hash_channel (Hash.md5 ()) ic
      |> transform_string (Hexa.encode ())
      |> print_endline
    )

let spec =
  let open Command.Spec in
  empty
  +> anon ("filename" %: string)

let command =
  Command.basic
    ~summary:"Generate an MD5 hash of the input data"
    ~readme: (fun () -> "More detailed information")
    spec
    (fun filename () -> do_hash filename)

let () =
  Command.run ~version: "1.0" ~build_info: "RWO" command
```

### Built with

- OCaml version: 4.06.0
- Core version: v0.10.0

```
corebuild -pkg cryptokit basic_cmd.native
```