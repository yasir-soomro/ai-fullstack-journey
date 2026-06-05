

// conditional statements 
// marks assign students to different classes based on their marks

let marks = 85

if (marks >= 90 && marks <= 100) {
    console.log("Grade A");
} else if (marks >= 80 && marks < 90) { 
    console.log("Grade B");
} else if (marks >= 70 && marks < 80) {
    console.log("Grade C");
} else {
    console.log("Grade D");
}


//  LOOPS  

// for = "repeat a known number of times"
// while = "repeat until a condition changes"

// 1 — Login System 

let attempts: number = 0;
const maxAttempts: number = 3;

let lockUntil: number | null = null;

function login(password: string): void {
  const now: number = Date.now();

  if (lockUntil !== null && now < lockUntil) {
    const minutesLeft: number = Math.ceil(
      (lockUntil - now) / 1000 / 60
    );

    console.log(
      `Account locked. Try again in ${minutesLeft} minute(s).`
    );

    return;
  }

  if (password === "admin123") {
    console.log("Login successful");

    attempts = 0;
    lockUntil = null;

    return;
  }

  attempts++;

  console.log(
    `Wrong password. Attempts left: ${
      maxAttempts - attempts
    }`
  );

  if (attempts >= maxAttempts) {
    lockUntil = Date.now() + 5 * 60 * 1000;

    attempts = 0;

    console.log(
      "Too many attempts. Account locked for 5 minutes."
    );
  }
}
