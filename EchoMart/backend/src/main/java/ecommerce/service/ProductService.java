package com.example.ecommerce.service;

import com.example.ecommerce.model.Product;
import com.example.ecommerce.repository.ProductRepository; // Import your repository
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository; // Inject your product repository

    // Method to search products by name
    public List<Product> searchProductsByName(String query) {
        List<Product> allProducts = productRepository.findAll();  // Fetch all products from the database
        
        // Filter the products whose name contains the search query (case-insensitive)
        return allProducts.stream()
                          .filter(product -> product.getName().toLowerCase().contains(query.toLowerCase()))
                          .collect(Collectors.toList());
    }
}