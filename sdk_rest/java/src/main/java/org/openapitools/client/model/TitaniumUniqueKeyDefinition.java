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
import java.util.ArrayList;
import java.util.List;

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
 * TitaniumUniqueKeyDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-07T12:58:40.226232Z[UTC]")
public class TitaniumUniqueKeyDefinition {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ORDER = "order";
  @SerializedName(SERIALIZED_NAME_ORDER)
  private String order;

  public static final String SERIALIZED_NAME_ORDER_BY = "orderBy";
  @SerializedName(SERIALIZED_NAME_ORDER_BY)
  private List<String> orderBy = null;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_UNIQUE_KEY = "uniqueKey";
  @SerializedName(SERIALIZED_NAME_UNIQUE_KEY)
  private List<String> uniqueKey = null;

  public TitaniumUniqueKeyDefinition() { 
  }

  public TitaniumUniqueKeyDefinition name(String name) {
    
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public TitaniumUniqueKeyDefinition order(String order) {
    
    this.order = order;
    return this;
  }

   /**
   * Get order
   * @return order
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOrder() {
    return order;
  }


  public void setOrder(String order) {
    this.order = order;
  }


  public TitaniumUniqueKeyDefinition orderBy(List<String> orderBy) {
    
    this.orderBy = orderBy;
    return this;
  }

  public TitaniumUniqueKeyDefinition addOrderByItem(String orderByItem) {
    if (this.orderBy == null) {
      this.orderBy = new ArrayList<>();
    }
    this.orderBy.add(orderByItem);
    return this;
  }

   /**
   * Get orderBy
   * @return orderBy
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getOrderBy() {
    return orderBy;
  }


  public void setOrderBy(List<String> orderBy) {
    this.orderBy = orderBy;
  }


  public TitaniumUniqueKeyDefinition scope(String scope) {
    
    this.scope = scope;
    return this;
  }

   /**
   * Get scope
   * @return scope
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getScope() {
    return scope;
  }


  public void setScope(String scope) {
    this.scope = scope;
  }


  public TitaniumUniqueKeyDefinition uniqueKey(List<String> uniqueKey) {
    
    this.uniqueKey = uniqueKey;
    return this;
  }

  public TitaniumUniqueKeyDefinition addUniqueKeyItem(String uniqueKeyItem) {
    if (this.uniqueKey == null) {
      this.uniqueKey = new ArrayList<>();
    }
    this.uniqueKey.add(uniqueKeyItem);
    return this;
  }

   /**
   * Get uniqueKey
   * @return uniqueKey
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getUniqueKey() {
    return uniqueKey;
  }


  public void setUniqueKey(List<String> uniqueKey) {
    this.uniqueKey = uniqueKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumUniqueKeyDefinition titaniumUniqueKeyDefinition = (TitaniumUniqueKeyDefinition) o;
    return Objects.equals(this.name, titaniumUniqueKeyDefinition.name) &&
        Objects.equals(this.order, titaniumUniqueKeyDefinition.order) &&
        Objects.equals(this.orderBy, titaniumUniqueKeyDefinition.orderBy) &&
        Objects.equals(this.scope, titaniumUniqueKeyDefinition.scope) &&
        Objects.equals(this.uniqueKey, titaniumUniqueKeyDefinition.uniqueKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, order, orderBy, scope, uniqueKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumUniqueKeyDefinition {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    order: ").append(toIndentedString(order)).append("\n");
    sb.append("    orderBy: ").append(toIndentedString(orderBy)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    uniqueKey: ").append(toIndentedString(uniqueKey)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("order");
    openapiFields.add("orderBy");
    openapiFields.add("scope");
    openapiFields.add("uniqueKey");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumUniqueKeyDefinition
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumUniqueKeyDefinition.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumUniqueKeyDefinition is not found in the empty JSON string", TitaniumUniqueKeyDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumUniqueKeyDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumUniqueKeyDefinition` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("name") != null && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("order") != null && !jsonObj.get("order").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order").toString()));
      }
      // ensure the json data is an array
      if (jsonObj.get("orderBy") != null && !jsonObj.get("orderBy").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `orderBy` to be an array in the JSON string but got `%s`", jsonObj.get("orderBy").toString()));
      }
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      // ensure the json data is an array
      if (jsonObj.get("uniqueKey") != null && !jsonObj.get("uniqueKey").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `uniqueKey` to be an array in the JSON string but got `%s`", jsonObj.get("uniqueKey").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumUniqueKeyDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumUniqueKeyDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumUniqueKeyDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumUniqueKeyDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumUniqueKeyDefinition>() {
           @Override
           public void write(JsonWriter out, TitaniumUniqueKeyDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumUniqueKeyDefinition read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumUniqueKeyDefinition given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumUniqueKeyDefinition
  * @throws IOException if the JSON string is invalid with respect to TitaniumUniqueKeyDefinition
  */
  public static TitaniumUniqueKeyDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumUniqueKeyDefinition.class);
  }

 /**
  * Convert an instance of TitaniumUniqueKeyDefinition to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

