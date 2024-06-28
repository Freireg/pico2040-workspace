cmake_minimum_required(VERSION 3.13)

# initialize the SDK based on PICO_SDK_PATH
# note: this must happen before project()
include(pico_sdk_import.cmake)

project(my_project)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

set(WIFI_SSID "${WIFI_SSID}" CACHE INTERNAL "WiFi SSID for examples")
set(WIFI_PASSWORD "${WIFI_PASSWORD}" CACHE INTERNAL "WiFi password for examples")

if ("${WIFI_SSID}" STREQUAL "")
    message("Skipping some Pico W examples as WIFI_SSID is not defined")
elseif ("${WIFI_PASSWORD}" STREQUAL "")
    message("Skipping some Pico W examples as WIFI_PASSWORD is not defined")
else()
    add_subdirectory(iperf)
    add_subdirectory(ntp_client)
    add_subdirectory(tcp_client)
    add_subdirectory(tcp_server)
    add_subdirectory(freertos)
    add_subdirectory(udp_beacon)

    if (NOT PICO_MBEDTLS_PATH)
        message("Skipping tls examples as PICO_MBEDTLS_PATH is not defined")
    else()
        add_subdirectory(tls_client)
    endif()
endif()


add_executable(picow_wifi_scan_background
        src/picow_wifi_scan.c
        )
target_include_directories(picow_wifi_scan_background PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        ${CMAKE_CURRENT_LIST_DIR}/inc # for our common lwipopts
        )
target_link_libraries(picow_wifi_scan_background
        pico_cyw43_arch_lwip_threadsafe_background
        pico_stdlib
        )

pico_add_extra_outputs(picow_wifi_scan_background)

add_executable(picow_wifi_scan_poll
        src/picow_wifi_scan.c
        )
target_include_directories(picow_wifi_scan_poll PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        ${CMAKE_CURRENT_LIST_DIR}/inc # for our common lwipopts
        )
target_link_libraries(picow_wifi_scan_poll
        pico_cyw43_arch_lwip_poll
        pico_stdlib
        )
pico_add_extra_outputs(picow_wifi_scan_poll)

