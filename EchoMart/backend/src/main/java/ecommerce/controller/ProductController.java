package ecommerce.controller;

import ecommerce..models.Product;
import com.ecommerce.repositories.ProductRepository;

import ecommerce.model.Product;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class ProductController {

    @Autowired
    private ProductRepository productRepository;

    @GetMapping("/search")
    public List<Product> searchProducts(@RequestParam String query) {
        return productRepository.findByNameContaining(query); // Query database for matching products
    }
}
