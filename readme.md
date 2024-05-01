![Lenskart Products & Stores Scrapping](https://wikimug.com/wp-content/uploads/2024/02/wikimug-post-pics-2-750x375.png)
# Scrapping Lenskart

> We will have to use concept of infinite scroll for scrapping products, since the below products are getting loaded only when we scroll it till there

# Links:
- **Sunglasses**: https://www.lenskart.com/sunglasses.html?product_type=Sunglasses
- **Eyeglasses**: https://www.lenskart.com/eyeglasses.html?product_type=Eyeglasses
- **Contact-Lenses**: https://www.lenskart.com/eyeglasses.html?product_type=Contact+Lens

- **Stores**: https://stores.lenskart.com/open-stores-list

---


    Problem faced while directly implementing scroll to bottom, as the content was still not loading. It needed to scroll to just above the footer for the content to load. 
    
    Solution: Using scroll by a specified small value
---

    Also Contact Lenses don't have size property, so I used usage