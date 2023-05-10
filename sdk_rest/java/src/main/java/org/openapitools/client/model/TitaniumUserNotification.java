/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.TitaniumAssetM;
import org.openapitools.client.model.TitaniumMarket;
import org.openapitools.client.model.TitaniumUser;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumUserNotification
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-10T19:13:00.376912Z[UTC]")
public class TitaniumUserNotification {
  public static final String SERIALIZED_NAME_ASSET = "asset";
  @SerializedName(SERIALIZED_NAME_ASSET)
  private TitaniumAssetM asset;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MARKET = "market";
  @SerializedName(SERIALIZED_NAME_MARKET)
  private TitaniumMarket market;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_USER = "user";
  @SerializedName(SERIALIZED_NAME_USER)
  private TitaniumUser user;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public TitaniumUserNotification() { 
  }

  public TitaniumUserNotification asset(TitaniumAssetM asset) {
    
    this.asset = asset;
    return this;
  }

   /**
   * Get asset
   * @return asset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumAssetM getAsset() {
    return asset;
  }


  public void setAsset(TitaniumAssetM asset) {
    this.asset = asset;
  }


  public TitaniumUserNotification id(String id) {
    
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getId() {
    return id;
  }


  public void setId(String id) {
    this.id = id;
  }


  public TitaniumUserNotification market(TitaniumMarket market) {
    
    this.market = market;
    return this;
  }

   /**
   * Get market
   * @return market
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumMarket getMarket() {
    return market;
  }


  public void setMarket(TitaniumMarket market) {
    this.market = market;
  }


  public TitaniumUserNotification type(String type) {
    
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getType() {
    return type;
  }


  public void setType(String type) {
    this.type = type;
  }


  public TitaniumUserNotification user(TitaniumUser user) {
    
    this.user = user;
    return this;
  }

   /**
   * Get user
   * @return user
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumUser getUser() {
    return user;
  }


  public void setUser(TitaniumUser user) {
    this.user = user;
  }


  public TitaniumUserNotification value(String value) {
    
    this.value = value;
    return this;
  }

   /**
   * Get value
   * @return value
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getValue() {
    return value;
  }


  public void setValue(String value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUserNotification titaniumUserNotification = (TitaniumUserNotification) o;
    return Objects.equals(this.asset, titaniumUserNotification.asset) &&
        Objects.equals(this.id, titaniumUserNotification.id) &&
        Objects.equals(this.market, titaniumUserNotification.market) &&
        Objects.equals(this.type, titaniumUserNotification.type) &&
        Objects.equals(this.user, titaniumUserNotification.user) &&
        Objects.equals(this.value, titaniumUserNotification.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(asset, id, market, type, user, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUserNotification {\n");
    sb.append("    asset: ").append(toIndentedString(asset)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    market: ").append(toIndentedString(market)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("asset");
    openapiFields.add("id");
    openapiFields.add("market");
    openapiFields.add("type");
    openapiFields.add("user");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUserNotification
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUserNotification.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUserNotification is not found in the empty JSON string", TitaniumUserNotification.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUserNotification.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUserNotification` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `asset`
      if (jsonObj.getAsJsonObject("asset") != null) {
        TitaniumAssetM.validateJsonObject(jsonObj.getAsJsonObject("asset"));
      }
      if (jsonObj.get("id") != null && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `market`
      if (jsonObj.getAsJsonObject("market") != null) {
        TitaniumMarket.validateJsonObject(jsonObj.getAsJsonObject("market"));
      }
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `user`
      if (jsonObj.getAsJsonObject("user") != null) {
        TitaniumUser.validateJsonObject(jsonObj.getAsJsonObject("user"));
      }
      if (jsonObj.get("value") != null && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUserNotification.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUserNotification' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUserNotification> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUserNotification.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUserNotification>() {
           @Override
           public void write(JsonWriter out, TitaniumUserNotification value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUserNotification read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUserNotification given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUserNotification
  * @throws IOException if the JSON string is invalid with respect to TitaniumUserNotification
  */
  public static TitaniumUserNotification fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUserNotification.class);
  }

 /**
  * Convert an instance of TitaniumUserNotification to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

