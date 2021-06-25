export default function getOptions() {
  // console.log(facID);
  const flightPlanCoordinates1 = [
    { lat: 40.689247, lng: -74.004502 },
    { lat: 40.699247, lng: -74.024502 },
  ]

  const flightPlanCoordinates2 = [ 
    { lat: 40.689247, lng: -74.044502 },
    { lat: 40.709247, lng: -74.064502 },
  ]

  const flightPath1 = {
    path: flightPlanCoordinates1,
    geodesic: true,
    strokeColor: '#9D2D23',
    strokeOpacity: 0.8,
    strokeWeight: 4,
    facID: "001",
  }

  const flightPath2 = {
    path: flightPlanCoordinates2,
    geodesic: true,
    strokeColor: '#9D2D23',
    strokeOpacity: 0.8,
    strokeWeight: 4,
    facID: "002",
  }

  return [flightPath1, flightPath2];
}