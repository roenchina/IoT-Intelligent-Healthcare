export default function getOptions() {
  // zIndex按照时间排序
  const markerOptions = [
    {
      position: { lat: 40.689247, lng: -74.044502 },
      label: "√",
      title: "LADY LIBERTY",
      facID: "002",
      zIndex: 0,
      info: "设备号：002",
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
    },
    {
      position: { lat: 40.689247, lng: -74.004502 },
      label: "√",
      title: "LADY LIBERTY",
      facID: "001",
      zIndex: 1,
      info: "设备号：001",
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
    },
    {
      position: { lat: 40.699247, lng: -74.024502 },
      label: "×",
      title: "LADY LIBERTY",
      facID: "001",
      zIndex: 2,
      info: "设备号：001",
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",\
    },
    {
      position: { lat: 40.709247, lng: -74.064502 },
      label: "×",
      title: "LADY LIBERTY",
      facID: "002",
      zIndex: 3,
      info: "设备号：002",
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",\
    },
  ];

  return markerOptions;
}