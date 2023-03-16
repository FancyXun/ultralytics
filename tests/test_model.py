from ultralytics.nn.tasks import DetectionModel

model = DetectionModel(cfg='yolov8l.yaml')
print(model)
