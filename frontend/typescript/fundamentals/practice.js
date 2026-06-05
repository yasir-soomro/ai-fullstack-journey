// 1 — Login Check
var isLoggedIn = false;
if (isLoggedIn) {
    console.log("Welcome back, user!");
}
else {
    console.log("Please log in to continue.");
}
// 2 — Admin Dashboard
var role = "admin";
if (role === "admin") {
    console.log("Access granted to admin dashboard.");
}
else if (role === "user") {
    console.log("Access granted to user dashboard.");
}
else {
    console.log("Access denied. Please log in.");
}
// 3 — Product List
// Loop through:
var products = ["Phone", "Laptop", "Mouse"];
for (var _i = 0, products_1 = products; _i < products_1.length; _i++) {
    var product = products_1[_i];
    console.log(product);
}
