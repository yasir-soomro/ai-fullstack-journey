

// practice of functions in TypeScript. Functions are reusable blocks of code that perform a specific task. They can take parameters, return values, and be called multiple times throughout your code.

// 1 — Basic Function

function greet(name: string): void {
  console.log(`Hello, ${name}!`);
}

greet("Alice"); // Output: Hello, Alice!


// Recommended Order

// Start with easier features and gradually increase complexity:

// 1. register()
// 2. login()
// 3. resetPassword()
// 4. sendOTP()
// 5. createTask()
// 6. completeTask()
// 7. addToCart()
// 8. checkout()
// 9. placeOrder()
// 10. cancelOrder()
// 11. uploadFile()

type RegisterInput = {
  username: string;
  email: string;
  password: string;
};

type User = {
  username: string;
  email: string;
  password: string;
};

function register(data: RegisterInput): User {

  if (!data.username) {
    throw new Error("Username is required");
  }

  if (!data.email) {
    throw new Error("Email is required");
  }

  if (data.password.length < 5) {
    throw new Error(
      "Password must be at least 5 characters"
    );
  }

  return {
    username: data.username,
    email: data.email,
    password: data.password,
  };
}