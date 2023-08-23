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
import org.openapitools.client.model.TitaniumUsage;

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
 * TitaniumDependency
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-23T13:58:25.807183Z[UTC]")
public class TitaniumDependency {
  public static final String SERIALIZED_NAME_ENTITY = "entity";
  @SerializedName(SERIALIZED_NAME_ENTITY)
  private String entity;

  public static final String SERIALIZED_NAME_ENTITY_NAME = "entityName";
  @SerializedName(SERIALIZED_NAME_ENTITY_NAME)
  private String entityName;

  public static final String SERIALIZED_NAME_ENTITY_TYPE = "entityType";
  @SerializedName(SERIALIZED_NAME_ENTITY_TYPE)
  private String entityType;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_USAGES = "usages";
  @SerializedName(SERIALIZED_NAME_USAGES)
  private List<TitaniumUsage> usages = null;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public TitaniumDependency() { 
  }

  public TitaniumDependency entity(String entity) {
    
    this.entity = entity;
    return this;
  }

   /**
   * Get entity
   * @return entity
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEntity() {
    return entity;
  }


  public void setEntity(String entity) {
    this.entity = entity;
  }


  public TitaniumDependency entityName(String entityName) {
    
    this.entityName = entityName;
    return this;
  }

   /**
   * Get entityName
   * @return entityName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEntityName() {
    return entityName;
  }


  public void setEntityName(String entityName) {
    this.entityName = entityName;
  }


  public TitaniumDependency entityType(String entityType) {
    
    this.entityType = entityType;
    return this;
  }

   /**
   * Get entityType
   * @return entityType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEntityType() {
    return entityType;
  }


  public void setEntityType(String entityType) {
    this.entityType = entityType;
  }


  public TitaniumDependency scope(String scope) {
    
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


  public TitaniumDependency usages(List<TitaniumUsage> usages) {
    
    this.usages = usages;
    return this;
  }

  public TitaniumDependency addUsagesItem(TitaniumUsage usagesItem) {
    if (this.usages == null) {
      this.usages = new ArrayList<>();
    }
    this.usages.add(usagesItem);
    return this;
  }

   /**
   * Get usages
   * @return usages
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumUsage> getUsages() {
    return usages;
  }


  public void setUsages(List<TitaniumUsage> usages) {
    this.usages = usages;
  }


  public TitaniumDependency version(String version) {
    
    this.version = version;
    return this;
  }

   /**
   * Get version
   * @return version
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getVersion() {
    return version;
  }


  public void setVersion(String version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumDependency titaniumDependency = (TitaniumDependency) o;
    return Objects.equals(this.entity, titaniumDependency.entity) &&
        Objects.equals(this.entityName, titaniumDependency.entityName) &&
        Objects.equals(this.entityType, titaniumDependency.entityType) &&
        Objects.equals(this.scope, titaniumDependency.scope) &&
        Objects.equals(this.usages, titaniumDependency.usages) &&
        Objects.equals(this.version, titaniumDependency.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entity, entityName, entityType, scope, usages, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumDependency {\n");
    sb.append("    entity: ").append(toIndentedString(entity)).append("\n");
    sb.append("    entityName: ").append(toIndentedString(entityName)).append("\n");
    sb.append("    entityType: ").append(toIndentedString(entityType)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    usages: ").append(toIndentedString(usages)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("entity");
    openapiFields.add("entityName");
    openapiFields.add("entityType");
    openapiFields.add("scope");
    openapiFields.add("usages");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumDependency
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumDependency.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumDependency is not found in the empty JSON string", TitaniumDependency.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumDependency.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumDependency` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("entity") != null && !jsonObj.get("entity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity").toString()));
      }
      if (jsonObj.get("entityName") != null && !jsonObj.get("entityName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entityName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entityName").toString()));
      }
      if (jsonObj.get("entityType") != null && !jsonObj.get("entityType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entityType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entityType").toString()));
      }
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      JsonArray jsonArrayusages = jsonObj.getAsJsonArray("usages");
      if (jsonArrayusages != null) {
        // ensure the json data is an array
        if (!jsonObj.get("usages").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `usages` to be an array in the JSON string but got `%s`", jsonObj.get("usages").toString()));
        }

        // validate the optional field `usages` (array)
        for (int i = 0; i < jsonArrayusages.size(); i++) {
          TitaniumUsage.validateJsonObject(jsonArrayusages.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("version") != null && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumDependency.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumDependency' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumDependency> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumDependency.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumDependency>() {
           @Override
           public void write(JsonWriter out, TitaniumDependency value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumDependency read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumDependency given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumDependency
  * @throws IOException if the JSON string is invalid with respect to TitaniumDependency
  */
  public static TitaniumDependency fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumDependency.class);
  }

 /**
  * Convert an instance of TitaniumDependency to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

