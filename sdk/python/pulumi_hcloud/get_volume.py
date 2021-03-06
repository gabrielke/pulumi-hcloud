# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetVolumeResult:
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, id=None, labels=None, linux_device=None, location=None, name=None, selector=None, server=None, size=None, with_selector=None, with_statuses=None):
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        __self__.id = id
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        __self__.labels = labels
        if linux_device and not isinstance(linux_device, str):
            raise TypeError("Expected argument 'linux_device' to be a str")
        __self__.linux_device = linux_device
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if selector and not isinstance(selector, str):
            raise TypeError("Expected argument 'selector' to be a str")
        if selector is not None:
            warnings.warn("Please use the with_selector property instead.", DeprecationWarning)
            pulumi.log.warn("selector is deprecated: Please use the with_selector property instead.")

        __self__.selector = selector
        if server and not isinstance(server, str):
            raise TypeError("Expected argument 'server' to be a str")
        __self__.server = server
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        __self__.size = size
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        __self__.with_selector = with_selector
        if with_statuses and not isinstance(with_statuses, list):
            raise TypeError("Expected argument 'with_statuses' to be a list")
        __self__.with_statuses = with_statuses
class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            id=self.id,
            labels=self.labels,
            linux_device=self.linux_device,
            location=self.location,
            name=self.name,
            selector=self.selector,
            server=self.server,
            size=self.size,
            with_selector=self.with_selector,
            with_statuses=self.with_statuses)

def get_volume(id=None,location=None,name=None,selector=None,server=None,with_selector=None,with_statuses=None,opts=None):
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()


    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['selector'] = selector
    __args__['server'] = server
    __args__['withSelector'] = with_selector
    __args__['withStatuses'] = with_statuses
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getVolume:getVolume', __args__, opts=opts).value

    return AwaitableGetVolumeResult(
        id=__ret__.get('id'),
        labels=__ret__.get('labels'),
        linux_device=__ret__.get('linuxDevice'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        selector=__ret__.get('selector'),
        server=__ret__.get('server'),
        size=__ret__.get('size'),
        with_selector=__ret__.get('withSelector'),
        with_statuses=__ret__.get('withStatuses'))
