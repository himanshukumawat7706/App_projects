// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const languageToggle = document.querySelector('.nav-language');
    const dropdown = document.querySelector('.language-dropdown');

    // Toggle dropdown on click
    languageToggle.addEventListener('click', function (event) {
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (event) {
        if (!languageToggle.contains(event.target)) {
            dropdown.style.display = 'none';
        }
    });
});
// scripts.js (add this to your existing JavaScript file)
document.addEventListener('DOMContentLoaded', function () {
    const languageToggle = document.querySelector('.nav-language');
    const dropdown = document.querySelector('.language-dropdown');
    
    // Existing code for language dropdown...
    
    const signInText = document.querySelector('.nav-signin span');
    const loginModal = document.getElementById('loginModal');
    const closeModal = document.getElementById('closeModal');


    // Close modal when clicking on the close button
    closeModal.addEventListener('click', function () {
        loginModal.style.display = 'none';
    });

    // Close modal when clicking outside of the modal content
    window.addEventListener('click', function (event) {
        if (event.target === loginModal) {
            loginModal.style.display = 'none';
        }
    });
});
// Sample Product Data (Replace this with real data from your backend if needed)
const products = [
    { name: 'T-Shirt', category: 'Clothes', image: 'images/tshirt.jpg', description: 'Comfortable cotton T-Shirt', mrp: '₹500' },
    { name: 'Sofa', category: 'Furniture', image: 'images/sofa.jpg', description: 'Luxury leather sofa', mrp: '₹20,000' },
    { name: 'iPhone', category: 'Mobiles', image: 'images/iphone.jpg', description: 'Latest Apple iPhone', mrp: '₹75,000' },
    // Add more products here with their MRPs
];


// Function to display products
function displayProducts(productList) {
    const shopSection = document.querySelector('.shop-section');
    shopSection.innerHTML = ''; // Clear previous products
    
    productList.forEach(product => {
        const productBox = `
        <div class="box">
            <div class="box-content">
                <h2>${product.name}</h2>
                <div class="box-img" style="background-image: url('${product.image}');"></div>
                <p>${product.description}</p>
                <p><strong>MRP: ${product.mrp}</strong></p>
                <p>See More</p>
            </div>
        </div>`;
        shopSection.innerHTML += productBox;
    });
}


// Function to filter products based on the search term
function searchProducts() {
    const searchTerm = document.querySelector('.search-input').value.toLowerCase(); // Assuming your search input has class 'search-input'
    const filteredProducts = products.filter(product => 
        product.name.toLowerCase().includes(searchTerm)
    );
    displayProducts(filteredProducts); // Display the filtered products
}

// Event listener for search button click
document.getElementById('searchButton').addEventListener('click', searchProducts);

// Optionally, you can trigger search on pressing 'Enter'
document.getElementById('searchInput').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        searchProducts();
    }
});
document.querySelector('.search-icon').addEventListener('click', searchProducts); // Assuming your search button has class 'search-icon'

// Optionally, trigger search on pressing 'Enter'
document.querySelector('.search-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        searchProducts();
    }
});
async function searchProducts() {
    const searchTerm = document.querySelector('.search-input').value.toLowerCase(); // Get search term
    const response = await fetch(`http://localhost:8080/api/search?query=${searchTerm}`);
    
    if (response.ok) {
        const filteredProducts = await response.json(); // Parse JSON response
        displayProducts(filteredProducts); // Display the filtered products
    } else {
        console.error('Error fetching products:', response.statusText);
    }
}

// Event listener for search button click
document.getElementById('searchButton').addEventListener('click', searchProducts);

// Optionally, you can trigger search on pressing 'Enter'
document.getElementById('searchInput').addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        searchProducts();
    }
});

