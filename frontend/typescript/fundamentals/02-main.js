// conditional statements 
// marks assign students to different classes based on their marks
var marks = 85;
if (marks >= 90 && marks <= 100) {
    console.log("Grade A");
}
else if (marks >= 80 && marks < 90) {
    console.log("Grade B");
}
else if (marks >= 70 && marks < 80) {
    console.log("Grade C");
}
else {
    console.log("Grade D");
}
//  LOOPS  
// 1 — Login System 
var attempts = 0;
var maxAttempts = 3;
while (attempts < maxAttempts) {
    console.log("Try again please your Attempts Left", maxAttempts - attempts);
    attempts++;
}
