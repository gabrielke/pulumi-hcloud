# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetImageResult:
    """
    A collection of values returned by getImage.
    """
    def __init__(__self__, created=None, deprecated=None, description=None, id=None, labels=None, most_recent=None, name=None, os_flavor=None, os_version=None, rapid_deploy=None, selector=None, type=None, with_selector=None, with_statuses=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        __self__.created = created
        if deprecated and not isinstance(deprecated, str):
            raise TypeError("Expected argument 'deprecated' to be a str")
        __self__.deprecated = deprecated
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        __self__.id = id
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        __self__.labels = labels
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        __self__.most_recent = most_recent
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if os_flavor and not isinstance(os_flavor, str):
            raise TypeError("Expected argument 'os_flavor' to be a str")
        __self__.os_flavor = os_flavor
        if os_version and not isinstance(os_version, str):
            raise TypeError("Expected argument 'os_version' to be a str")
        __self__.os_version = os_version
        if rapid_deploy and not isinstance(rapid_deploy, bool):
            raise TypeError("Expected argument 'rapid_deploy' to be a bool")
        __self__.rapid_deploy = rapid_deploy
        if selector and not isinstance(selector, str):
            raise TypeError("Expected argument 'selector' to be a str")
        if selector is not None:
            warnings.warn("Please use the with_selector property instead.", DeprecationWarning)
            pulumi.log.warn("selector is deprecated: Please use the with_selector property instead.")

        __self__.selector = selector
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        __self__.with_selector = with_selector
        if with_statuses and not isinstance(with_statuses, list):
            raise TypeError("Expected argument 'with_statuses' to be a list")
        __self__.with_statuses = with_statuses
class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            created=self.created,
            deprecated=self.deprecated,
            description=self.description,
            id=self.id,
            labels=self.labels,
            most_recent=self.most_recent,
            name=self.name,
            os_flavor=self.os_flavor,
            os_version=self.os_version,
            rapid_deploy=self.rapid_deploy,
            selector=self.selector,
            type=self.type,
            with_selector=self.with_selector,
            with_statuses=self.with_statuses)

def get_image(id=None,most_recent=None,name=None,selector=None,with_selector=None,with_statuses=None,opts=None):
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()


    __args__['id'] = id
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['selector'] = selector
    __args__['withSelector'] = with_selector
    __args__['withStatuses'] = with_statuses
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getImage:getImage', __args__, opts=opts).value

    return AwaitableGetImageResult(
        created=__ret__.get('created'),
        deprecated=__ret__.get('deprecated'),
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        labels=__ret__.get('labels'),
        most_recent=__ret__.get('mostRecent'),
        name=__ret__.get('name'),
        os_flavor=__ret__.get('osFlavor'),
        os_version=__ret__.get('osVersion'),
        rapid_deploy=__ret__.get('rapidDeploy'),
        selector=__ret__.get('selector'),
        type=__ret__.get('type'),
        with_selector=__ret__.get('withSelector'),
        with_statuses=__ret__.get('withStatuses'))
