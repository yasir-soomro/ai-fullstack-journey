

// 1 — Login Check


const isLoggedIn = false


if (isLoggedIn) {
    console.log("Welcome back, user!")
}
else {
    console.log("Please log in to continue.")
}

// 2 — Admin Dashboard

const role = "admin";

if (role === "admin") {
    console.log("Access granted to admin dashboard.")
}
else if (role === "user") {
    console.log("Access granted to user dashboard.")
}

else {
    console.log("Access denied. Please log in.")
}