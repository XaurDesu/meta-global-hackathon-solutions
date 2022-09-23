use std::*;

fn main() {
    println!("Hello, world!");
    let mut file = File::open("../pipelines.txt");
    let reader = BufReader::new(file);
    
    for line in buf_reader.lines() {
        println!("{}", line?);
       }
}
