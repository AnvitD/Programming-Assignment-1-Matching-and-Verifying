# Programming-Assignment-1-Matching-and-Verifying

Anvit Dhamnekar
UFID: 15965003

Kalim Qazi
UFID: 85459363

How to complie/run this project: Make sure you have the input.txt file in the same directory(Prog 1) as the main.py. Then all you have to do is run the project -> python main.py. You will see the output in the output.txt file. 

The matching alogrithm will work with main.py. For the verify function you will have to run the verify.py file (python verify.py). For this also make sure the output.txt is in the same directory. You will see the output in the terminal. Do not change the formatting of either the input or output files. 

You can add more test cases to the input.txt file. However, you have to be carefull and follow the format of the previous test cases. 

Assumptions: The algorithm follows a hospital-centric view. 

Graph: For GS Algortihm

<img width="640" height="480" alt="gsalgoscal" src="https://github.com/user-attachments/assets/7ca571e9-efb5-4363-acc5-a8c917b58d49" />\

Graph: For Verification

<img width="640" height="480" alt="VerifierScalability" src="https://github.com/user-attachments/assets/8569d3fc-d083-4329-a2c8-3dc9e1f8e905" />

Comparing Scalability:

As the number of hospitals/students gets bigger, both the matching engine and the verifier get slower, the time starts to rise much faster once n gets large (especially around 128 → 256 → 512). So the trend is: small n = basically instant, but bigger n = time climbs quickly, and the verifier and the algorithm both show the same kind of steep upward curve (with the verifier usually a bit faster).
