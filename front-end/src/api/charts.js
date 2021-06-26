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


// 每个data对应一个marker元素
export function getAllMarkers() {
  return request({
    url: '/charts/getAllMarkers',
    method: 'get',
  });
}

// 每个设备对应一个polyline元素
export function getAllPolyline() {
  return request({
    url: '/charts/getAllPolyline',
    method: 'get',
  });
}