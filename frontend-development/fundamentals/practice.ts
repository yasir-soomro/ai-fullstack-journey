

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

// 3 — Product List

// Loop through:

  let products =    ["Phone", "Laptop", "Mouse"]

  for (let product of products) {  
     
    console.log(product)

   }
    
// Cart Discount

// If total > 10000:

// apply 20% discount

// Else:

// no discount


let total = 12000

if (total > 10000) {
    console.log("apply 20% discount");
    
} else {
    console.log(" no discount");
    
}


// Notification Filter

// Show only unread notifications.

let notifications = [
    { id: 1, message: "New message from John", read: false },
    { id: 2, message: "Your order has been shipped", read: true },
    { id: 3, message: "New comment on your post", read: false }
]

let unreadNotifications = notifications.filter(notification => !notification.read);

console.log(unreadNotifications);


