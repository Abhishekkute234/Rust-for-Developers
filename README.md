<h1> RUST For Developer</h1>

![My Image Description](https://external-preview.redd.it/announcing-rust-1-80-1-v0-x-d-Y1Pv5uu2Eh_7Ed1N0qkJqPf6qYHu3g1XDX9amZw.jpg?auto=webp&s=674b921c4a5871f7f2b58e506c6a2f06cc4f4ee1)

# Run the installation command in your terminal for UBUNTU

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

# After installation, ensure Rust is installed by running:

```
rustc --version
```

# Create a New Rust Project:

```
cargo new project_name
cd project_name
```

# Run the Project

```
cargo run
```

# TO run the paticular rust file in the src folder

```
cd src
rustc filename.rs
./filename
```

<p></p>When you run the cargo run command out of the src folder, it will automatically compile and run the main.rs file.In Cargo.toml file there are the dependences , name and the version of the cargo .Go to the the following command to chech the other commands in the cargo</p>

```
cargo help
```

# Rust Variables are imutable by default to make them mutable we use mut key work ,also the new()denotes the empty string.Here the {} is pass as an argument

```
    let mut guess: String =String :: new();
        println!("You guessed: {}", guess);// here the {} is pass as an argument

```

# To built the librarie in work

```
cargo build

```

# this is the library use to genearte random numbers

```
rand = "0.8.3"
```

# To generate the random number between 1 and 101

```
    let secret_number=rand:: thread_rug().gen_range(low:1, high:101);
```
