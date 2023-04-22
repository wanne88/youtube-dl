const express = require('express');
const ytdl = require('ytdl-core');
const app = express();

app.get('/download', (req, res) => {
  const url = req.query.videoUrl;
  res.header('Content-Disposition', 'attachment; filename="video.mp4"');
  ytdl(url, {
    format: 'mp4'
  }).on('data', (chunk) => {
    res.write(chunk);
  }).on('end', () => {
    res.end();
  });
});

const port = process.env.PORT || 54264;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
