import request from '@/utils/request';

// format
// [
//   { value: 78, name: "online" },
//   { value: 38, name: "offline" },
//   { value: 22, name: "error" },
// ]
export function getFacPie() {
  return request({
    url: '/charts/getFacPie',
    method: 'get',
  });
}

// format
// [
//   { value: 78, name: "normal" },
//   { value: 8, name: "warning" },
// ]
export function getDataPie() {
  return request({
    url: '/charts/getDataPie',
    method: 'get',
  });
}

export function getAllLine() {
  return request({
    url: '/charts/getAllLine',
    method: 'get',
  });
}


// map
export function getMarkers() {
  return request({
    url: '/charts/getMarkers',
    method: 'get',
  });
}