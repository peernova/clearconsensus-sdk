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
import org.openapitools.client.model.TitaniumTransformation;

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
 * TitaniumNormalizationRuleDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-25T14:35:11.651542Z[UTC]")
public class TitaniumNormalizationRuleDefinition {
  public static final String SERIALIZED_NAME_DESCRIPTOR_NAME = "descriptorName";
  @SerializedName(SERIALIZED_NAME_DESCRIPTOR_NAME)
  private String descriptorName;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_TRANSFORMATIONS = "transformations";
  @SerializedName(SERIALIZED_NAME_TRANSFORMATIONS)
  private List<TitaniumTransformation> transformations = null;

  public static final String SERIALIZED_NAME_UID = "uid";
  @SerializedName(SERIALIZED_NAME_UID)
  private String uid;

  public TitaniumNormalizationRuleDefinition() { 
  }

  public TitaniumNormalizationRuleDefinition descriptorName(String descriptorName) {
    
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


  public TitaniumNormalizationRuleDefinition scope(String scope) {
    
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


  public TitaniumNormalizationRuleDefinition transformations(List<TitaniumTransformation> transformations) {
    
    this.transformations = transformations;
    return this;
  }

  public TitaniumNormalizationRuleDefinition addTransformationsItem(TitaniumTransformation transformationsItem) {
    if (this.transformations == null) {
      this.transformations = new ArrayList<>();
    }
    this.transformations.add(transformationsItem);
    return this;
  }

   /**
   * Get transformations
   * @return transformations
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumTransformation> getTransformations() {
    return transformations;
  }


  public void setTransformations(List<TitaniumTransformation> transformations) {
    this.transformations = transformations;
  }


  public TitaniumNormalizationRuleDefinition uid(String uid) {
    
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
    TitaniumNormalizationRuleDefinition titaniumNormalizationRuleDefinition = (TitaniumNormalizationRuleDefinition) o;
    return Objects.equals(this.descriptorName, titaniumNormalizationRuleDefinition.descriptorName) &&
        Objects.equals(this.scope, titaniumNormalizationRuleDefinition.scope) &&
        Objects.equals(this.transformations, titaniumNormalizationRuleDefinition.transformations) &&
        Objects.equals(this.uid, titaniumNormalizationRuleDefinition.uid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(descriptorName, scope, transformations, uid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumNormalizationRuleDefinition {\n");
    sb.append("    descriptorName: ").append(toIndentedString(descriptorName)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    transformations: ").append(toIndentedString(transformations)).append("\n");
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
    openapiFields.add("descriptorName");
    openapiFields.add("scope");
    openapiFields.add("transformations");
    openapiFields.add("uid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumNormalizationRuleDefinition
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumNormalizationRuleDefinition.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumNormalizationRuleDefinition is not found in the empty JSON string", TitaniumNormalizationRuleDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumNormalizationRuleDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumNormalizationRuleDefinition` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("descriptorName") != null && !jsonObj.get("descriptorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `descriptorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("descriptorName").toString()));
      }
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      JsonArray jsonArraytransformations = jsonObj.getAsJsonArray("transformations");
      if (jsonArraytransformations != null) {
        // ensure the json data is an array
        if (!jsonObj.get("transformations").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `transformations` to be an array in the JSON string but got `%s`", jsonObj.get("transformations").toString()));
        }

        // validate the optional field `transformations` (array)
        for (int i = 0; i < jsonArraytransformations.size(); i++) {
          TitaniumTransformation.validateJsonObject(jsonArraytransformations.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("uid") != null && !jsonObj.get("uid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumNormalizationRuleDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumNormalizationRuleDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumNormalizationRuleDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumNormalizationRuleDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumNormalizationRuleDefinition>() {
           @Override
           public void write(JsonWriter out, TitaniumNormalizationRuleDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumNormalizationRuleDefinition read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumNormalizationRuleDefinition given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumNormalizationRuleDefinition
  * @throws IOException if the JSON string is invalid with respect to TitaniumNormalizationRuleDefinition
  */
  public static TitaniumNormalizationRuleDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumNormalizationRuleDefinition.class);
  }

 /**
  * Convert an instance of TitaniumNormalizationRuleDefinition to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

