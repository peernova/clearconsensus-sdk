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
import org.openapitools.client.model.TitaniumRulesetDefinition;

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
 * TitaniumValidationRuleDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T11:33:57.346198Z[UTC]")
public class TitaniumValidationRuleDefinition {
  public static final String SERIALIZED_NAME_DEFINITION = "definition";
  @SerializedName(SERIALIZED_NAME_DEFINITION)
  private TitaniumRulesetDefinition definition;

  public static final String SERIALIZED_NAME_DESCRIPTOR_NAME = "descriptorName";
  @SerializedName(SERIALIZED_NAME_DESCRIPTOR_NAME)
  private String descriptorName;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_UID = "uid";
  @SerializedName(SERIALIZED_NAME_UID)
  private String uid;

  public TitaniumValidationRuleDefinition() { 
  }

  public TitaniumValidationRuleDefinition definition(TitaniumRulesetDefinition definition) {
    
    this.definition = definition;
    return this;
  }

   /**
   * Get definition
   * @return definition
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRulesetDefinition getDefinition() {
    return definition;
  }


  public void setDefinition(TitaniumRulesetDefinition definition) {
    this.definition = definition;
  }


  public TitaniumValidationRuleDefinition descriptorName(String descriptorName) {
    
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


  public TitaniumValidationRuleDefinition scope(String scope) {
    
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


  public TitaniumValidationRuleDefinition uid(String uid) {
    
    this.uid = uid;
    return this;
  }

   /**
   * Get uid
   * @return uid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUid() {
    return uid;
  }


  public void setUid(String uid) {
    this.uid = uid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumValidationRuleDefinition titaniumValidationRuleDefinition = (TitaniumValidationRuleDefinition) o;
    return Objects.equals(this.definition, titaniumValidationRuleDefinition.definition) &&
        Objects.equals(this.descriptorName, titaniumValidationRuleDefinition.descriptorName) &&
        Objects.equals(this.scope, titaniumValidationRuleDefinition.scope) &&
        Objects.equals(this.uid, titaniumValidationRuleDefinition.uid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(definition, descriptorName, scope, uid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumValidationRuleDefinition {\n");
    sb.append("    definition: ").append(toIndentedString(definition)).append("\n");
    sb.append("    descriptorName: ").append(toIndentedString(descriptorName)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    uid: ").append(toIndentedString(uid)).append("\n");
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
    openapiFields.add("definition");
    openapiFields.add("descriptorName");
    openapiFields.add("scope");
    openapiFields.add("uid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumValidationRuleDefinition
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumValidationRuleDefinition.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumValidationRuleDefinition is not found in the empty JSON string", TitaniumValidationRuleDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumValidationRuleDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumValidationRuleDefinition` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `definition`
      if (jsonObj.getAsJsonObject("definition") != null) {
        TitaniumRulesetDefinition.validateJsonObject(jsonObj.getAsJsonObject("definition"));
      }
      if (jsonObj.get("descriptorName") != null && !jsonObj.get("descriptorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `descriptorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("descriptorName").toString()));
      }
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      if (jsonObj.get("uid") != null && !jsonObj.get("uid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumValidationRuleDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumValidationRuleDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumValidationRuleDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumValidationRuleDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumValidationRuleDefinition>() {
           @Override
           public void write(JsonWriter out, TitaniumValidationRuleDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumValidationRuleDefinition read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumValidationRuleDefinition given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumValidationRuleDefinition
  * @throws IOException if the JSON string is invalid with respect to TitaniumValidationRuleDefinition
  */
  public static TitaniumValidationRuleDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumValidationRuleDefinition.class);
  }

 /**
  * Convert an instance of TitaniumValidationRuleDefinition to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

