const app = require("express")();
const server = require("http").createServer(app);
const io = require("socket.io")(server);

const connection = require("./db.js");

let country = require("./country.js");

async function getCountryData(countryName, category) {
  const [rows, fields] = await (
    await connection
  ).execute(
    `SELECT * FROM globalnewsweb WHERE country = '${countryName}' AND category = '${category}' ORDER BY createdAt DESC LIMIT 5`
  );

  return rows;
}

async function getCountryDataAll() {
  const result = [];
  const category = ["정치", "경제", "스포츠"];

  for (let i = 0; i < country.length; i++) {
    const dic = {};
    dic["name"] = country[i].name;

    for (let j = 0; j < category.length; j++) {
      dic["category"] = category[j];

      const data = await getCountryData(country[i].name, category[j]);
      const info = { url: [], title: [] };

      for (let i = 0; i < data.length; i++) {
        info.url.push(data[i].url);
        info.title.push(data[i].title);
      }

      dic[category[j]] = info;
    }

    result.push(dic);
  }
  return result;
}

app.use(require("express").static("public"));

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/public/main.html");
});

app.get("/map", function (req, res) {
  res.sendFile(__dirname + "/public/map.html");
});

server.listen(3000, function () {
  console.log("Socket IO server listening on port 3000");
});

io.on("connection", function (socket) {
  socket.on("pin", async function (f) {
    const data = await getCountryData(f.country, f.category);

    const info = { url: [], title: [] };

    for (let i = 0; i < data.length; i++) {
      info.url.push(data[i].url);
      info.title.push(data[i].title);
    }

    console.log(info);

    socket.emit("ping", info);
  });
});
