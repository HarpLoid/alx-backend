import express, { json } from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

// Promisify Redis methods
const hgetAsync = promisify(client.hget).bind(client);
const hsetAsync = promisify(client.hset).bind(client);

// Array of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}

// Reserve stock by item ID
async function reserveStockById(itemId, stock) {
  await hsetAsync(`item.${itemId}`, 'stock', stock);
}

// Get current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const stock = await hgetAsync(`item.${itemId}`, 'stock');
  console.log(stock);
  return parseInt(stock) || 0;
}

// Middleware to parse JSON
app.use(json());

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const productDetails = { ...product, currentQuantity };
  res.json(productDetails);
});

// Route to reserve product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
