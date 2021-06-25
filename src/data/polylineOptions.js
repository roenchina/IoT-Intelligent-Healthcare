export default function getOptions() {
  // console.log(facID);
  const flightPlanCoordinates = [
    { lat: 40.689247, lng: -74.004502 },
    { lat: 40.699247, lng: -74.024502 },
    { lat: 40.689247, lng: -74.044502 },
    { lat: 40.709247, lng: -74.064502 },
  ]
  const flightPath = {
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#9D2D23',
    strokeOpacity: 0.8,
    strokeWeight: 4,
  }

  return flightPath;
}