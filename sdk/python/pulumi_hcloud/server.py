# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class Server(pulumi.CustomResource):
    backup_window: pulumi.Output[str]
    backups: pulumi.Output[bool]
    datacenter: pulumi.Output[str]
    image: pulumi.Output[str]
    ipv4_address: pulumi.Output[str]
    ipv6_address: pulumi.Output[str]
    ipv6_network: pulumi.Output[str]
    iso: pulumi.Output[str]
    keep_disk: pulumi.Output[bool]
    labels: pulumi.Output[dict]
    location: pulumi.Output[str]
    name: pulumi.Output[str]
    rescue: pulumi.Output[str]
    server_type: pulumi.Output[str]
    ssh_keys: pulumi.Output[list]
    status: pulumi.Output[str]
    user_data: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, backups=None, datacenter=None, image=None, iso=None, keep_disk=None, labels=None, location=None, name=None, rescue=None, server_type=None, ssh_keys=None, user_data=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a Server resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
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

            __props__['backups'] = backups
            __props__['datacenter'] = datacenter
            if image is None:
                raise TypeError("Missing required property 'image'")
            __props__['image'] = image
            __props__['iso'] = iso
            __props__['keep_disk'] = keep_disk
            __props__['labels'] = labels
            __props__['location'] = location
            __props__['name'] = name
            __props__['rescue'] = rescue
            if server_type is None:
                raise TypeError("Missing required property 'server_type'")
            __props__['server_type'] = server_type
            __props__['ssh_keys'] = ssh_keys
            __props__['user_data'] = user_data
            __props__['backup_window'] = None
            __props__['ipv4_address'] = None
            __props__['ipv6_address'] = None
            __props__['ipv6_network'] = None
            __props__['status'] = None
        super(Server, __self__).__init__(
            'hcloud:index/server:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, backup_window=None, backups=None, datacenter=None, image=None, ipv4_address=None, ipv6_address=None, ipv6_network=None, iso=None, keep_disk=None, labels=None, location=None, name=None, rescue=None, server_type=None, ssh_keys=None, status=None, user_data=None):
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backup_window"] = backup_window
        __props__["backups"] = backups
        __props__["datacenter"] = datacenter
        __props__["image"] = image
        __props__["ipv4_address"] = ipv4_address
        __props__["ipv6_address"] = ipv6_address
        __props__["ipv6_network"] = ipv6_network
        __props__["iso"] = iso
        __props__["keep_disk"] = keep_disk
        __props__["labels"] = labels
        __props__["location"] = location
        __props__["name"] = name
        __props__["rescue"] = rescue
        __props__["server_type"] = server_type
        __props__["ssh_keys"] = ssh_keys
        __props__["status"] = status
        __props__["user_data"] = user_data
        return Server(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
