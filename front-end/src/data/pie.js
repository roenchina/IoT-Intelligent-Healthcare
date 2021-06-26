function random() {
  return Math.round(300 + Math.random() * 700) / 10;
}

export default function getPie() {
  return {
    textStyle: {
      fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    },
    title: {
      text: "设备状况一览",
      left: "center"
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
      orient: "vertical",
      left: "left",
      data: ["Online", "Offline", "Error"]
    },
    series: [
      {
        name: "设备状况一览",
        type: "pie",
        radius: "55%",
        center: ["50%", "60%"],
        data: [
          { value: random(), name: "Online" },
          { value: random(), name: "Offline" },
          { value: random(), name: "Error" },
        ],
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)"
          }
        }
      }
    ]
  };
}
