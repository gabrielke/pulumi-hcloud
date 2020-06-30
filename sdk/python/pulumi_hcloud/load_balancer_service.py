# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class LoadBalancerService(pulumi.CustomResource):
    destination_port: pulumi.Output[float]
    health_check: pulumi.Output[dict]
    http: pulumi.Output[dict]
    listen_port: pulumi.Output[float]
    load_balancer_id: pulumi.Output[str]
    protocol: pulumi.Output[str]
    proxyprotocol: pulumi.Output[bool]
    def __init__(__self__, resource_name, opts=None, destination_port=None, health_check=None, http=None, listen_port=None, load_balancer_id=None, protocol=None, proxyprotocol=None, __props__=None, __name__=None, __opts__=None):
        """
          Define services for Hetzner Cloud Load Balancers.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        The **health_check** object supports the following:

          * `http` (`pulumi.Input[dict]`)
            * `domain` (`pulumi.Input[str]`)
            * `path` (`pulumi.Input[str]`)
            * `response` (`pulumi.Input[str]`)
            * `statusCodes` (`pulumi.Input[list]`)
            * `tls` (`pulumi.Input[bool]`)

          * `interval` (`pulumi.Input[float]`)
          * `port` (`pulumi.Input[float]`)
          * `protocol` (`pulumi.Input[str]`)
          * `retries` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[float]`)

        The **http** object supports the following:

          * `certificates` (`pulumi.Input[list]`)
          * `cookieLifetime` (`pulumi.Input[float]`)
          * `cookieName` (`pulumi.Input[str]`)
          * `redirectHttp` (`pulumi.Input[bool]`)
          * `stickySessions` (`pulumi.Input[bool]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['destination_port'] = destination_port
            __props__['health_check'] = health_check
            __props__['http'] = http
            __props__['listen_port'] = listen_port
            if load_balancer_id is None:
                raise TypeError("Missing required property 'load_balancer_id'")
            __props__['load_balancer_id'] = load_balancer_id
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['proxyprotocol'] = proxyprotocol
        super(LoadBalancerService, __self__).__init__(
            'hcloud:index/loadBalancerService:LoadBalancerService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, destination_port=None, health_check=None, http=None, listen_port=None, load_balancer_id=None, protocol=None, proxyprotocol=None):
        """
        Get an existing LoadBalancerService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        The **health_check** object supports the following:

          * `http` (`pulumi.Input[dict]`)
            * `domain` (`pulumi.Input[str]`)
            * `path` (`pulumi.Input[str]`)
            * `response` (`pulumi.Input[str]`)
            * `statusCodes` (`pulumi.Input[list]`)
            * `tls` (`pulumi.Input[bool]`)

          * `interval` (`pulumi.Input[float]`)
          * `port` (`pulumi.Input[float]`)
          * `protocol` (`pulumi.Input[str]`)
          * `retries` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[float]`)

        The **http** object supports the following:

          * `certificates` (`pulumi.Input[list]`)
          * `cookieLifetime` (`pulumi.Input[float]`)
          * `cookieName` (`pulumi.Input[str]`)
          * `redirectHttp` (`pulumi.Input[bool]`)
          * `stickySessions` (`pulumi.Input[bool]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["destination_port"] = destination_port
        __props__["health_check"] = health_check
        __props__["http"] = http
        __props__["listen_port"] = listen_port
        __props__["load_balancer_id"] = load_balancer_id
        __props__["protocol"] = protocol
        __props__["proxyprotocol"] = proxyprotocol
        return LoadBalancerService(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
