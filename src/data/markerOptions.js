export default function getOptions() {
  // zIndex按照时间排序
  const markerOptions = [
    {
      position: { lat: 40.689247, lng: -74.044502 },
      label: "√",
      title: "LADY LIBERTY",
      zIndex: 0,
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
    },
    {
      position: { lat: 40.689247, lng: -74.004502 },
      label: "√",
      title: "LADY LIBERTY",
      zIndex: 1,
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
    },
    {
      position: { lat: 40.699247, lng: -74.024502 },
      label: "×",
      title: "LADY LIBERTY",
      zIndex: 2,
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",\
    },
    {
      position: { lat: 40.709247, lng: -74.064502 },
      label: "×",
      title: "LADY LIBERTY",
      zIndex: 3,
      // icon: "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",\
    },
  ];

  return markerOptions;
}