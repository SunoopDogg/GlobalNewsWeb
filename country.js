const country = [
  { name: "브라질", lat: -15.7801, lng: -47.9292 },
  { name: "멕시코", lat: 19.4326, lng: -99.1332 },
  { name: "인도네시아", lat: -6.2088, lng: 106.8456 },
  { name: "사우디아라비아", lat: 24.7743, lng: 46.7388 },
  { name: "튀르키예", lat: 38.9637, lng: 35.2433 },
  { name: "아르헨티나", lat: -34.6037, lng: -58.3816 },
  { name: "남아프리카공화국", lat: -30.5595, lng: 22.9375 },
  { name: "그리스", lat: 37.9838, lng: 23.7275 },
  { name: "필리핀", lat: 14.5995, lng: 120.9842 },
  { name: "태국", lat: 13.7563, lng: 100.5018 },
  { name: "미국", lat: 37.0902, lng: -95.7129 },
  { name: "중국", lat: 39.9042, lng: 116.4074 },
  { name: "일본", lat: 35.6762, lng: 139.6503 },
  { name: "영국", lat: 51.5074, lng: -0.1278 },
  { name: "프랑스", lat: 48.8566, lng: 2.3522 },
  { name: "캐나다", lat: 45.4215, lng: -75.6972 },
  { name: "대한민국", lat: 37.5665, lng: 126.978 },
  { name: "러시아", lat: 55.7558, lng: 37.6173 },
  { name: "호주", lat: -33.8688, lng: 151.2093 },
  { name: "스웨덴", lat: 59.3293, lng: 18.0686 },
  { name: "스페인", lat: 40.4168, lng: -3.7038 },
  { name: "말레시아", lat: 3.139, lng: 101.6869 },
  { name: "독일", lat: 52.52, lng: 13.405 },
  { name: "오스트리아", lat: 48.2082, lng: 16.3738 },
  { name: "폴란드", lat: 52.2297, lng: 21.0122 },
  { name: "이탈리아", lat: 41.9028, lng: 12.4964 },
  { name: "벨기에", lat: 50.8503, lng: 4.3517 },
];

country.sort((a, b) => {
  if (a.name < b.name) return -1;
  if (a.name > b.name) return 1;
  return 0;
});

module.exports = country;
