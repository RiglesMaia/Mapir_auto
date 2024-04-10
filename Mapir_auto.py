#@R.Maia
#

import time
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys

def data_input(x):
    for i in range(x):
        SendKeys('{ENTER}')
        time.sleep(2)

def wait_process(mapir):
    while True:
        process_button = mapir.MAPIRCameraControl.child_window(title="Process",
                                                              auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.widget1.Left_Side2.processPushButton",
                                                              control_type="Button").wrapper_object()
        if process_button.is_enabled():
            break
        time.sleep(1)

def image_process(pasta, conectar=True):
    if conectar:
        mapir = Application(backend='uia').connect(title='MAPIR Camera Control (MCC)', timeout=15)
    else:
        mapir = Application(backend='uia').start('/Users/Rigles Maia/Desktop/DESKTOP/PROGRAMAS/MAPIR Camera Control 20230407.exe').connect(title='MAPIR Camera Control (MCC)', timeout=15)
        mapir.MAPIRCameraControl.print_control_identifiers()

    data_input = mapir.MAPIRCameraControl.child_window(title=" Input",
                                                       auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.verticalWidget.PreProcessInButton",
                                                       control_type="Button").wrapper_object()
    data_input.click_input()
    SendKeys(pasta)

    for i in range(2):
        SendKeys('{ENTER}')

    data_analyse = mapir.MAPIRCameraControl.child_window(title="Analyze",
                                                         auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.widget1.Left_Side2.analyzePushButton",
                                                         control_type="Button").wrapper_object()

    data_analyse.click_input()

    time.sleep(2)

    Vignette_cor = mapir.MAPIRCameraControl.child_window(title="Vignette (Flat Field) Correction",
                                                         auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.widget1.Left_Side2.PreProcessVignette",
                                                         control_type="CheckBox").wrapper_object()

    Vignette_cor.click_input()

    time.sleep(2)

    image_type = mapir.MAPIRCameraControl.child_window(auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.widget1.Left_Side2.horizontalWidget",
                                                       control_type="Group").wrapper_object()

    image_type.click_input()

    time.sleep(2)

    slect_image_type = mapir.MAPIRCameraControl.child_window(title="JPG (8-bit)", control_type="ListItem").wrapper_object()

    slect_image_type.click_input()

    time.sleep(2)

    process = mapir.MAPIRCameraControl.child_window(title="Process",
                                                    auto_id="MAPIR_ProcessingDockWidgetBase.dockWidgetContents.MapirTab.qt_tabwidget_stackedwidget.Process.widget.widget1.Left_Side2.processPushButton",
                                                    control_type="Button").wrapper_object()

    process.click_input()

    wait_process(mapir)


data = ["RGN", "REDEDGE"]

for pasta in data:
    image_process(pasta, conectar=(pasta != data[0]))
