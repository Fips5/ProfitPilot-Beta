const PORT = process.env.PORT || 8000;
const express = require('express');
const fs = require('fs');

const app = express();

async function getPriceFromJson() {
  try {
    const filePath = 'C:/Users/David/Desktop/API Manual/Webcam Model/output.json';
    const data = await fs.promises.readFile(filePath, 'utf8');
    const jsonData = JSON.parse(data);
    const price = jsonData.price[0]; // Assuming the "price" property is an array with one value
    price = price.replace('.', ',');
    const timestamp = new Date().toLocaleString();

    const dataToSave = {
      symbol: 'TSLA',
      prices: [price], // Save the price as an array, matching the original data structure
      timestamp,
    };

    fs.writeFile('price_data.json', '', (err) => {
      if (err) {
        console.error('Error creating JSON file:', err);
      }
    });

    fs.appendFile('price_data.json', JSON.stringify(dataToSave) + '\n', 'utf8', (err) => {
      if (err) {
        console.error('Error appending to JSON file:', err);
      }
    });
  } catch (err) {
    console.error(err);
  }
}

setInterval(getPriceFromJson, 2000);

app.get('/', (req, res) => {
  fs.readFile('price_data.json', 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading JSON file:', err);
      return res.status(500).send('Internal Server Error');
    }

    try {
      const jsonData = JSON.parse(data);
      res.json(jsonData);
    } catch (err) {
      console.error('Error parsing JSON:', err);
      return res.status(500).send('Internal Server Error');
    }
  });
});

app.listen(PORT, () => console.log(`Server running on PORT: ${PORT}`));
