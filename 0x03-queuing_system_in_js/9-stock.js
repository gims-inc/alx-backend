const redis = require('redis');
const { promisify } = require('util');
const express = require('express');

const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

// return the item from listProducts with the same id
const getItemById = (id) => listProducts.find((item) => item.id === Number(id));

const app = express();
const client = redis.createClient();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

const getAsync = promisify(client.get).bind(client);
// set in Redis the stock for the key item.ITEM_ID
const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock);
};
// return the reserved stock for a specific item
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(itemId);
  return stock;
};

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const stock = await getCurrentReservedStockById(itemId);

  if (!item) res.json({ status: 'Product not found' });

  item.currentQuantity = stock;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const stock = await getCurrentReservedStockById(itemId);

  if (!item) res.json({ status: 'Product not found' });

  if (stock >= 1) {
    reserveStockById(itemId, stock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }

  res.json({ status: 'Not enough stock available', itemId });
});

app.listen(port, () => {
  listProducts.forEach((element) => {
    reserveStockById(element.id, element.initialAvailableQuantity);
  });
  console.log(`API available on localhost port ${port}`);
});
