// practice of functions in TypeScript. Functions are reusable blocks of code that perform a specific task. They can take parameters, return values, and be called multiple times throughout your code.
// 1 — Basic Function
function greet(name) {
    console.log("Hello, ".concat(name, "!"));
}
greet("Alice"); // Output: Hello, Alice!
function register(username, useremail, password) {
    return {
        username: username,
        useremail: useremail,
        password: password
    };
}
var res = register("Afzal Soomro", "afzalsoomro@gmail.com", "soomro0311");
console.log(res);
