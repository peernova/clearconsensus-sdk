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
import org.openapitools.client.model.TitaniumIdentifier;

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
 * TitaniumGetDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-06-30T14:58:59.766741Z[UTC]")
public class TitaniumGetDefinition {
  public static final String SERIALIZED_NAME_DESCRIPTOR_NAME = "descriptorName";
  @SerializedName(SERIALIZED_NAME_DESCRIPTOR_NAME)
  private String descriptorName;

  public static final String SERIALIZED_NAME_IDENTIFIER = "identifier";
  @SerializedName(SERIALIZED_NAME_IDENTIFIER)
  private TitaniumIdentifier identifier;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public TitaniumGetDefinition() { 
  }

  public TitaniumGetDefinition descriptorName(String descriptorName) {
    
    this.descriptorName = descriptorName;
    return this;
  }

   /**
   * Get descriptorName
   * @return descriptorName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDescriptorName() {
    return descriptorName;
  }


  public void setDescriptorName(String descriptorName) {
    this.descriptorName = descriptorName;
  }


  public TitaniumGetDefinition identifier(TitaniumIdentifier identifier) {
    
    this.identifier = identifier;
    return this;
  }

   /**
   * Get identifier
   * @return identifier
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumIdentifier getIdentifier() {
    return identifier;
  }


  public void setIdentifier(TitaniumIdentifier identifier) {
    this.identifier = identifier;
  }


  public TitaniumGetDefinition scope(String scope) {
    
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumGetDefinition titaniumGetDefinition = (TitaniumGetDefinition) o;
    return Objects.equals(this.descriptorName, titaniumGetDefinition.descriptorName) &&
        Objects.equals(this.identifier, titaniumGetDefinition.identifier) &&
        Objects.equals(this.scope, titaniumGetDefinition.scope);
  }

  @Override
  public int hashCode() {
    return Objects.hash(descriptorName, identifier, scope);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumGetDefinition {\n");
    sb.append("    descriptorName: ").append(toIndentedString(descriptorName)).append("\n");
    sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
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
    openapiFields.add("descriptorName");
    openapiFields.add("identifier");
    openapiFields.add("scope");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumGetDefinition
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumGetDefinition.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumGetDefinition is not found in the empty JSON string", TitaniumGetDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumGetDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumGetDefinition` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("descriptorName") != null && !jsonObj.get("descriptorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `descriptorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("descriptorName").toString()));
      }
      // validate the optional field `identifier`
      if (jsonObj.getAsJsonObject("identifier") != null) {
        TitaniumIdentifier.validateJsonObject(jsonObj.getAsJsonObject("identifier"));
      }
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumGetDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumGetDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumGetDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumGetDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumGetDefinition>() {
           @Override
           public void write(JsonWriter out, TitaniumGetDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumGetDefinition read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumGetDefinition given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumGetDefinition
  * @throws IOException if the JSON string is invalid with respect to TitaniumGetDefinition
  */
  public static TitaniumGetDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumGetDefinition.class);
  }

 /**
  * Convert an instance of TitaniumGetDefinition to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

