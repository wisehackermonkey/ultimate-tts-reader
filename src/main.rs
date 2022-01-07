use std::io;
use inputbot::{BlockInput::*, KeybdKey::*, MouseButton::*, *};
use std::{thread::sleep, time::Duration};
use tts::*;
use tts::*;
fn text_to_speech(text: &str)  -> Result<(), Error>  {
    let mut tts = Tts::default()?;
    tts.speak(text,false);
    Ok(())
}
fn main() -> Result<(), Error> {
    // env_logger::init();
    let  mut tts = Tts::default().unwrap(); 
    tts.speak("wow",false).unwrap(); 

    println!("Press Enter and wait for speech.");
      InsertKey.bind(|| { 
          println!("Insert Key");
          let  mut tts = Tts::default().unwrap(); 
          tts.speak("wow".to_owned(),false).unwrap(); 
        
});
    // loop {
    //     let mut _input = String::new();
    //     io::stdin().read_line(&mut _input)?;
    //     tts.speak("Hello, world.", true)?;
    // }
    inputbot::handle_input_events();
    handle_input_events();
    Ok(())
}
// use inputbot::{BlockInput::*, KeybdKey::*, MouseButton::*, *};
// use std::{thread::sleep, time::Duration};
// use tts::*;
// use std::io;
// fn main() {
//     // env_logger::init();
//     let mut tts = Tts::default();
//     tts.speak("Insert + left shift", true);

//     InsertKey.bind(|| println!("Insert"));
//     // Autorun for videogames.
//     LShiftKey.bind(|| {
//         while InsertKey.is_pressed() {
//             println!("Insert + left shift");
//             tts.speak("Insert + left shift", true);
//         }
//     });

     

//     inputbot::handle_input_events();
     
//     InsertKey.blockable_bind(|| {
//         if LShiftKey.is_pressed() {
//             Block
//         } else {
//             DontBlock
//         }
//     });

//     // Block the A key when left shift is held.
//     KKey.block_bind(|| ());

//     // Call this to start listening for bound inputs.
//     handle_input_events();
//     //     loop {
// //         let mut _input = String::new();
// //         io::stdin().read_line(&mut _input)?;
// //         tts.speak("Hello, world.", true)?;
// //     }
// }