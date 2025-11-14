Crazy Prophet is a text-generation project built using a custom-trained LSTM neural network.
The model is trained on a collection of literary, mystical, and archaic texts to generate new “prophecies” in a dramatic and poetic style.

HOW TO USE:
1.Clone the repository:
	
	git clone https://github.com/Saskato/crazy-prophet.git
	cd crazy-prophet

2.Install dependencies:
	
	pip install -r requirements.txt

3.Run the cleaner:
	
	python src/cleaner.py

This will:
remove numbers
remove unusual characters
normalize whitespace
lowercase everything

4.Train the LSTM model:

	python src/trainer.py

This performs:
tokenization
sequence generation
LSTM model construction
training
saving of model + tokenizer
The output files appear in:
models/
    crazy_prophet.keras
    tokenizer.pkl

5.Now YOU can generate prophecies by running this file:
	
	python src/generator.py
Or by running this code in your program:
	
	from generator import generate

	print(generate(
    	seed="I see that you", #starting phrase for generation
    	length=20, #amounth of words generated
    	temperature=0.9 #temeperature determines how often generator going to pick the next predicted word. Higher temperature meanse the higher probability of not picking best prediction(put the value in range 0-2)
		
	))
