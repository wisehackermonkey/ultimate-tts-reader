// use std::sync::Arc;
// use std::thread;
// use tts::*;

// fn tts_rust(text: &str) -> Result<(), Error> {
//     Ok(())
// }

// fn main() -> Result<(), Error> {
//     let stack = vec!["wow", "rust", "is", "awesome"];

//     // loop {
//         let text = stack[0];
//         let mut tts = Tts::default()?;
//         tts.speak(text, false)?;
//     // }
//     Ok(())
// }
use std::{thread, time};
use std::sync::Arc;
use tts::*;
use std::io;
use inputbot::{BlockInput::*, KeybdKey::*, MouseButton::*, *};
fn main() -> Result<(), Error> {
     let mut tts = Tts::default()?;
 
    inputbot::handle_input_events();
    handle_input_events();
    loop { 
        tts.speak(format!("Phrase {}", local), true)?;
        let time = time::Duration::from_secs(5);
        thread::sleep(time);
        println!("local {}", local);
        // local += 1;
    }
}