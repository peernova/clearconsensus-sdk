/**
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ProtoServiceResponse from '../model/ProtoServiceResponse';
import ProtoUserDto from '../model/ProtoUserDto';
import RpcStatus from '../model/RpcStatus';
import TitaniumGetUserNotificationByMarketRequest from '../model/TitaniumGetUserNotificationByMarketRequest';
import TitaniumGetUserNotificationRequest from '../model/TitaniumGetUserNotificationRequest';
import TitaniumGetUserPermissionsRequest from '../model/TitaniumGetUserPermissionsRequest';
import TitaniumGetUserRequest from '../model/TitaniumGetUserRequest';
import TitaniumUserNotificationRequest from '../model/TitaniumUserNotificationRequest';
import TitaniumUserNotificationResponse from '../model/TitaniumUserNotificationResponse';
import TitaniumUserNotificationsResponse from '../model/TitaniumUserNotificationsResponse';
import TitaniumUserPermissionsResponse from '../model/TitaniumUserPermissionsResponse';
import TitaniumUserResponse from '../model/TitaniumUserResponse';

/**
* UserService service.
* @module api/UserServiceApi
* @version 1.0.0
*/
export default class UserServiceApi {

    /**
    * Constructs a new UserServiceApi. 
    * @alias module:api/UserServiceApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the userServiceAddUserNotification operation.
     * @callback module:api/UserServiceApi~userServiceAddUserNotificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserNotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumUserNotificationRequest} body 
     * @param {module:api/UserServiceApi~userServiceAddUserNotificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserNotificationResponse}
     */
    userServiceAddUserNotification(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceAddUserNotification");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserNotificationResponse;
      return this.apiClient.callApi(
        '/api/v1/user/notifications/add', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceCreate operation.
     * @callback module:api/UserServiceApi~userServiceCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProtoServiceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/ProtoUserDto} body 
     * @param {module:api/UserServiceApi~userServiceCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProtoServiceResponse}
     */
    userServiceCreate(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceCreate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = ProtoServiceResponse;
      return this.apiClient.callApi(
        '/api/v1/user-management/users/create', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceDeleteUserNotification operation.
     * @callback module:api/UserServiceApi~userServiceDeleteUserNotificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserNotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumUserNotificationRequest} body 
     * @param {module:api/UserServiceApi~userServiceDeleteUserNotificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserNotificationResponse}
     */
    userServiceDeleteUserNotification(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceDeleteUserNotification");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserNotificationResponse;
      return this.apiClient.callApi(
        '/api/v1/user/notifications/delete', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetAll operation.
     * @callback module:api/UserServiceApi~userServiceGetAllCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProtoServiceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Boolean} body 
     * @param {module:api/UserServiceApi~userServiceGetAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProtoServiceResponse}
     */
    userServiceGetAll(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetAll");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = ProtoServiceResponse;
      return this.apiClient.callApi(
        '/api/v1/user-management/users/getAll', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetById operation.
     * @callback module:api/UserServiceApi~userServiceGetByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProtoServiceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} body 
     * @param {module:api/UserServiceApi~userServiceGetByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProtoServiceResponse}
     */
    userServiceGetById(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetById");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = ProtoServiceResponse;
      return this.apiClient.callApi(
        '/api/v1/user-management/users/getById', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetUser operation.
     * @callback module:api/UserServiceApi~userServiceGetUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumGetUserRequest} body 
     * @param {module:api/UserServiceApi~userServiceGetUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserResponse}
     */
    userServiceGetUser(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetUser");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserResponse;
      return this.apiClient.callApi(
        '/api/v1/user', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetUserNotifications operation.
     * @callback module:api/UserServiceApi~userServiceGetUserNotificationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserNotificationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumGetUserNotificationRequest} body 
     * @param {module:api/UserServiceApi~userServiceGetUserNotificationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserNotificationsResponse}
     */
    userServiceGetUserNotifications(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetUserNotifications");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserNotificationsResponse;
      return this.apiClient.callApi(
        '/api/v1/user/notifications', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetUserNotificationsByMarket operation.
     * @callback module:api/UserServiceApi~userServiceGetUserNotificationsByMarketCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserNotificationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumGetUserNotificationByMarketRequest} body 
     * @param {module:api/UserServiceApi~userServiceGetUserNotificationsByMarketCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserNotificationsResponse}
     */
    userServiceGetUserNotificationsByMarket(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetUserNotificationsByMarket");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserNotificationsResponse;
      return this.apiClient.callApi(
        '/api/v1/user/notifications/market', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceGetUserPermissions operation.
     * @callback module:api/UserServiceApi~userServiceGetUserPermissionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserPermissionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumGetUserPermissionsRequest} body 
     * @param {module:api/UserServiceApi~userServiceGetUserPermissionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserPermissionsResponse}
     */
    userServiceGetUserPermissions(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceGetUserPermissions");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserPermissionsResponse;
      return this.apiClient.callApi(
        '/api/v1/user/permissions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceUpdate operation.
     * @callback module:api/UserServiceApi~userServiceUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProtoServiceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/ProtoUserDto} body 
     * @param {module:api/UserServiceApi~userServiceUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProtoServiceResponse}
     */
    userServiceUpdate(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceUpdate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = ProtoServiceResponse;
      return this.apiClient.callApi(
        '/api/v1/user-management/users/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userServiceUpdateUserNotification operation.
     * @callback module:api/UserServiceApi~userServiceUpdateUserNotificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TitaniumUserNotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/TitaniumUserNotificationRequest} body 
     * @param {module:api/UserServiceApi~userServiceUpdateUserNotificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TitaniumUserNotificationResponse}
     */
    userServiceUpdateUserNotification(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling userServiceUpdateUserNotification");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = TitaniumUserNotificationResponse;
      return this.apiClient.callApi(
        '/api/v1/user/notifications/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
